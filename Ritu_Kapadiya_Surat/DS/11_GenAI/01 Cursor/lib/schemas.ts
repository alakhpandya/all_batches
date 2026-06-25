import { z } from "zod";

export const keywordMatchSchema = z.object({
  keyword: z.string(),
  found: z.boolean(),
  source: z.enum(["hard_skill", "soft_skill", "tool"]),
});

export const formattingCheckSchema = z.object({
  singleColumn: z.boolean(),
  noTables: z.boolean(),
  standardSections: z.boolean(),
  plainTextSkills: z.boolean(),
});

export const evaluationSchema = z.object({
  score: z.number().min(0).max(100),
  breakdown: z.object({
    hardSkillKeywords: z.number().min(0).max(40),
    softSkillKeywords: z.number().min(0).max(20),
    contextualRelevance: z.number().min(0).max(20),
    formattingReadiness: z.number().min(0).max(20),
  }),
  keywordMatchList: z.array(keywordMatchSchema),
  formattingCompliance: formattingCheckSchema,
  feedback: z.array(z.string()),
});

export const changeLogEntrySchema = z.object({
  section: z.string(),
  original: z.string(),
  optimized: z.string(),
  reason: z.string(),
});

export const changeLogSchema = z.object({
  changes: z.array(changeLogEntrySchema),
});

export type EvaluationResult = z.infer<typeof evaluationSchema>;
export type ChangeLogResult = z.infer<typeof changeLogSchema>;
