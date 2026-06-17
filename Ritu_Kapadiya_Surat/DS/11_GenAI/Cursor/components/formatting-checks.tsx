"use client";

import { CheckCircle2, XCircle } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import type { FormattingCheck } from "@/lib/types";

interface FormattingChecksProps {
  compliance: FormattingCheck;
}

const CHECKS: {
  key: keyof FormattingCheck;
  label: string;
  failLabel: string;
}[] = [
  { key: "singleColumn", label: "Single Column", failLabel: "Multi-Column" },
  { key: "noTables", label: "No Tables", failLabel: "Tables Detected" },
  {
    key: "standardSections",
    label: "Standard Sections",
    failLabel: "Non-Standard Sections",
  },
  {
    key: "plainTextSkills",
    label: "Plain Text Skills",
    failLabel: "Formatted Skills",
  },
];

export function FormattingChecks({ compliance }: FormattingChecksProps) {
  return (
    <div className="flex flex-wrap gap-2">
      {CHECKS.map(({ key, label, failLabel }) => {
        const passed = compliance[key];
        return (
          <Badge
            key={key}
            variant={passed ? "success" : "warning"}
            className="flex items-center gap-1"
          >
            {passed ? (
              <CheckCircle2 className="h-3 w-3" />
            ) : (
              <XCircle className="h-3 w-3" />
            )}
            {passed ? label : failLabel}
          </Badge>
        );
      })}
    </div>
  );
}
