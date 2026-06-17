import { generateObject } from "ai";
import { evalModel } from "@/lib/ai";
import {
  EVALUATION_SYSTEM_PROMPT,
  buildEvaluationUserPrompt,
} from "@/lib/prompts";
import { evaluationSchema } from "@/lib/schemas";
import type { ATSEvaluation } from "@/lib/types";

export async function evaluateResume(
  resume: string,
  jobDescription: string
): Promise<ATSEvaluation> {
  const { object } = await generateObject({
    model: evalModel,
    schema: evaluationSchema,
    system: EVALUATION_SYSTEM_PROMPT,
    prompt: buildEvaluationUserPrompt(resume, jobDescription),
    temperature: 0.2,
  });

  const computedScore =
    object.breakdown.hardSkillKeywords +
    object.breakdown.softSkillKeywords +
    object.breakdown.contextualRelevance +
    object.breakdown.formattingReadiness;

  return {
    ...object,
    score: Math.min(100, Math.max(0, Math.round(computedScore))),
  };
}
