"use client";

import { ATSScoreRing } from "@/components/ats-score-ring";
import { FormattingChecks } from "@/components/formatting-checks";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import type { FormattingCheck, KeywordMatch } from "@/lib/types";

interface MetricsBarProps {
  finalScore: number;
  originalScore: number;
  keywordMatchList: KeywordMatch[];
  formattingCompliance: FormattingCheck;
  iterations: number;
}

export function MetricsBar({
  finalScore,
  originalScore,
  keywordMatchList,
  formattingCompliance,
  iterations,
}: MetricsBarProps) {
  const foundCount = keywordMatchList.filter((k) => k.found).length;
  const totalCount = keywordMatchList.length;
  const scoreDelta = finalScore - originalScore;

  return (
    <Card>
      <CardContent className="flex flex-col gap-6 p-6 md:flex-row md:items-center md:justify-between">
        <div className="flex items-center gap-6">
          <ATSScoreRing score={finalScore} />
          <div className="space-y-1">
            <p className="text-sm text-muted-foreground">Final ATS Score</p>
            <p className="text-lg font-semibold">
              {finalScore >= 85 ? "Target Met" : "Best Effort"}
              {scoreDelta !== 0 && (
                <span
                  className={`ml-2 text-sm font-normal ${scoreDelta > 0 ? "text-emerald-600" : "text-red-600"}`}
                >
                  ({scoreDelta > 0 ? "+" : ""}
                  {scoreDelta} from {originalScore})
                </span>
              )}
            </p>
            <p className="text-xs text-muted-foreground">
              Completed in {iterations} optimization{" "}
              {iterations === 1 ? "pass" : "passes"}
            </p>
          </div>
        </div>

        <div className="space-y-2">
          <p className="text-sm font-medium">Keyword Match Ratio</p>
          <Badge variant="secondary" className="text-sm">
            {foundCount}/{totalCount} critical keywords found
          </Badge>
          <div className="flex flex-wrap gap-1 pt-1">
            {keywordMatchList.map((kw) => (
              <Badge
                key={kw.keyword}
                variant={kw.found ? "success" : "outline"}
                className="text-xs"
              >
                {kw.keyword}
              </Badge>
            ))}
          </div>
        </div>

        <div className="space-y-2">
          <p className="text-sm font-medium">Formatting Compliance</p>
          <FormattingChecks compliance={formattingCompliance} />
        </div>
      </CardContent>
    </Card>
  );
}
