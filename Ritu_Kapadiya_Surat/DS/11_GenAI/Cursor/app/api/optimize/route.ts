import { runOptimizationLoop } from "@/lib/optimization-loop";
import type { OptimizeRequest, OptimizeErrorResponse } from "@/lib/types";

export const maxDuration = 120;

const MAX_INPUT_LENGTH = 15000;

export async function POST(req: Request) {
  try {
    if (!process.env.OPENAI_API_KEY) {
      return Response.json(
        { error: "OpenAI API key is not configured. Set OPENAI_API_KEY in .env.local." } satisfies OptimizeErrorResponse,
        { status: 500 }
      );
    }

    let body: OptimizeRequest;
    try {
      body = await req.json();
    } catch {
      return Response.json(
        { error: "Invalid JSON body." } satisfies OptimizeErrorResponse,
        { status: 400 }
      );
    }

    const resume = body.resume?.trim();
    const jobDescription = body.jobDescription?.trim();

    if (!resume || !jobDescription) {
      return Response.json(
        {
          error: "Both resume and job description are required.",
        } satisfies OptimizeErrorResponse,
        { status: 400 }
      );
    }

    if (resume.length > MAX_INPUT_LENGTH || jobDescription.length > MAX_INPUT_LENGTH) {
      return Response.json(
        {
          error: `Each input must be under ${MAX_INPUT_LENGTH} characters.`,
        } satisfies OptimizeErrorResponse,
        { status: 413 }
      );
    }

    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 115_000);

    try {
      const result = await Promise.race([
        runOptimizationLoop(resume, jobDescription),
        new Promise<never>((_, reject) => {
          controller.signal.addEventListener("abort", () =>
            reject(new Error("TIMEOUT"))
          );
        }),
      ]);

      return Response.json(result);
    } catch (err) {
      if (err instanceof Error && err.message === "TIMEOUT") {
        return Response.json(
          { error: "Optimization timed out. Please try again with shorter inputs." } satisfies OptimizeErrorResponse,
          { status: 504 }
        );
      }
      throw err;
    } finally {
      clearTimeout(timeout);
    }
  } catch (error) {
    console.error("Optimization error:", error);
    return Response.json(
      {
        error: "Failed to optimize resume. Please try again.",
      } satisfies OptimizeErrorResponse,
      { status: 500 }
    );
  }
}
