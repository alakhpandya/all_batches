import { evaluateResume } from "@/lib/ats-evaluator";
import { optimizeResume, generateChangeLog } from "@/lib/ats-optimizer";
import type { OptimizeResponse } from "@/lib/types";

const MAX_ITERATIONS = 3;
const TARGET_SCORE = 85;

export async function runOptimizationLoop(
  originalResume: string,
  jobDescription: string
): Promise<OptimizeResponse> {
  let currentResume = originalResume;
  let evaluation = await evaluateResume(currentResume, jobDescription);
  const originalScore = evaluation.score;
  let iterations = 0;

  while (evaluation.score < TARGET_SCORE && iterations < MAX_ITERATIONS) {
    currentResume = await optimizeResume(
      currentResume,
      jobDescription,
      evaluation
    );
    evaluation = await evaluateResume(currentResume, jobDescription);
    iterations++;
  }

  const changeLog = await generateChangeLog(originalResume, currentResume);

  return {
    optimizedResumeText: currentResume,
    originalScore,
    finalScore: evaluation.score,
    iterations,
    keywordMatchList: evaluation.keywordMatchList,
    formattingCompliance: evaluation.formattingCompliance,
    changeLog,
  };
}
