"use client";

import {
  Search,
  FileSearch,
  RefreshCw,
  FileCheck,
  CheckCircle2,
  Loader2,
} from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";

const STEPS = [
  {
    label: "Analyzing Job Description Keywords...",
    icon: Search,
  },
  {
    label: "Evaluating Original Resume Structure...",
    icon: FileSearch,
  },
  {
    label: "Executing Iterative ATS Scoring Loop...",
    icon: RefreshCw,
  },
  {
    label: "Finalizing Clean Text Formatting...",
    icon: FileCheck,
  },
];

interface ProcessingStageProps {
  currentStep: number;
}

export function ProcessingStage({ currentStep }: ProcessingStageProps) {
  const progress = ((currentStep + 1) / STEPS.length) * 100;

  return (
    <Card className="mx-auto max-w-2xl">
      <CardHeader className="text-center">
        <CardTitle className="text-xl">Optimizing Your Resume</CardTitle>
        <p className="text-sm text-muted-foreground">
          Running iterative ATS scoring and optimization...
        </p>
      </CardHeader>
      <CardContent className="space-y-8">
        <Progress value={progress} className="h-2" />

        <div className="space-y-4">
          {STEPS.map((step, index) => {
            const Icon = step.icon;
            const isComplete = index < currentStep;
            const isActive = index === currentStep;
            const isPending = index > currentStep;

            return (
              <div
                key={step.label}
                className={cn(
                  "flex items-center gap-4 rounded-lg border p-4 transition-all",
                  isActive && "border-primary bg-primary/5",
                  isComplete && "border-emerald-200 bg-emerald-50/50",
                  isPending && "opacity-50"
                )}
              >
                <div
                  className={cn(
                    "flex h-10 w-10 items-center justify-center rounded-full",
                    isActive && "bg-primary/10 text-primary",
                    isComplete && "bg-emerald-100 text-emerald-600",
                    isPending && "bg-muted text-muted-foreground"
                  )}
                >
                  {isComplete ? (
                    <CheckCircle2 className="h-5 w-5" />
                  ) : isActive ? (
                    <Loader2 className="h-5 w-5 animate-spin" />
                  ) : (
                    <Icon className="h-5 w-5" />
                  )}
                </div>
                <span
                  className={cn(
                    "text-sm font-medium",
                    isActive && "text-primary",
                    isComplete && "text-emerald-700"
                  )}
                >
                  {step.label}
                </span>
              </div>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}
