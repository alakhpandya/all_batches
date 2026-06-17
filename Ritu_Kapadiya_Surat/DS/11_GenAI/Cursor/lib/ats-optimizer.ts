import { generateText, generateObject } from "ai";
import { optimizeModel, evalModel } from "@/lib/ai";
import {
  OPTIMIZATION_SYSTEM_PROMPT,
  CHANGELOG_SYSTEM_PROMPT,
  buildOptimizationUserPrompt,
  buildChangeLogUserPrompt,
} from "@/lib/prompts";
import { changeLogSchema } from "@/lib/schemas";
import type { ATSEvaluation, ChangeLogEntry } from "@/lib/types";

export async function optimizeResume(
  resume: string,
  jobDescription: string,
  evaluation: ATSEvaluation
): Promise<string> {
  const missingKeywords = evaluation.keywordMatchList
    .filter((k) => !k.found)
    .map((k) => k.keyword);

  const { text } = await generateText({
    model: optimizeModel,
    system: OPTIMIZATION_SYSTEM_PROMPT,
    prompt: buildOptimizationUserPrompt(
      resume,
      jobDescription,
      evaluation.feedback,
      missingKeywords
    ),
    temperature: 0.4,
  });

  return text.trim();
}

export async function generateChangeLog(
  originalResume: string,
  optimizedResume: string
): Promise<ChangeLogEntry[]> {
  const { object } = await generateObject({
    model: evalModel,
    schema: changeLogSchema,
    system: CHANGELOG_SYSTEM_PROMPT,
    prompt: buildChangeLogUserPrompt(originalResume, optimizedResume),
    temperature: 0.2,
  });

  return object.changes;
}
