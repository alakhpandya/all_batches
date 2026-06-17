export interface OptimizeRequest {
  resume: string;
  jobDescription: string;
}

export interface KeywordMatch {
  keyword: string;
  found: boolean;
  source: "hard_skill" | "soft_skill" | "tool";
}

export interface FormattingCheck {
  singleColumn: boolean;
  noTables: boolean;
  standardSections: boolean;
  plainTextSkills: boolean;
}

export interface ATSEvaluation {
  score: number;
  breakdown: {
    hardSkillKeywords: number;
    softSkillKeywords: number;
    contextualRelevance: number;
    formattingReadiness: number;
  };
  keywordMatchList: KeywordMatch[];
  formattingCompliance: FormattingCheck;
  feedback: string[];
}

export interface ChangeLogEntry {
  section: string;
  original: string;
  optimized: string;
  reason: string;
}

export interface OptimizeResponse {
  optimizedResumeText: string;
  originalScore: number;
  finalScore: number;
  iterations: number;
  keywordMatchList: KeywordMatch[];
  formattingCompliance: FormattingCheck;
  changeLog: ChangeLogEntry[];
}

export interface OptimizeErrorResponse {
  error: string;
}
