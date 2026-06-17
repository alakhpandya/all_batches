"use client";

import { useState } from "react";
import { Copy, Download, RotateCcw, Check } from "lucide-react";
import { MetricsBar } from "@/components/metrics-bar";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import type { OptimizeResponse } from "@/lib/types";

interface OutputStageProps {
  data: OptimizeResponse;
  originalResume: string;
  onReset: () => void;
}

export function OutputStage({
  data,
  originalResume,
  onReset,
}: OutputStageProps) {
  const [optimizedText, setOptimizedText] = useState(
    data.optimizedResumeText
  );
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    await navigator.clipboard.writeText(optimizedText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  function handleExport() {
    const blob = new Blob([optimizedText], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "ats-optimized-resume.txt";
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="space-y-6">
      <MetricsBar
        finalScore={data.finalScore}
        originalScore={data.originalScore}
        keywordMatchList={data.keywordMatchList}
        formattingCompliance={data.formattingCompliance}
        iterations={data.iterations}
      />

      <div className="grid gap-6 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Original Resume</CardTitle>
            <CardDescription>Your submitted resume text</CardDescription>
          </CardHeader>
          <CardContent>
            <Textarea
              value={originalResume}
              readOnly
              className="min-h-[450px] resize-y bg-muted/30 font-mono text-sm"
            />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-lg">ATS-Optimized Resume</CardTitle>
            <CardDescription>
              Editable — tweak before copying or exporting
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Textarea
              value={optimizedText}
              onChange={(e) => setOptimizedText(e.target.value)}
              className="min-h-[450px] resize-y font-mono text-sm"
            />
          </CardContent>
        </Card>
      </div>

      {data.changeLog.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Optimization Change Log</CardTitle>
            <CardDescription>
              Key phrasing and structural improvements made
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {data.changeLog.map((entry, i) => (
                <div
                  key={`${entry.section}-${i}`}
                  className="rounded-lg border p-4 text-sm"
                >
                  <p className="font-medium text-primary">{entry.section}</p>
                  <div className="mt-2 grid gap-2 md:grid-cols-2">
                    <div>
                      <p className="text-xs text-muted-foreground">Before</p>
                      <p className="text-muted-foreground">{entry.original}</p>
                    </div>
                    <div>
                      <p className="text-xs text-muted-foreground">After</p>
                      <p>{entry.optimized}</p>
                    </div>
                  </div>
                  <p className="mt-2 text-xs text-muted-foreground">
                    {entry.reason}
                  </p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      <div className="flex flex-wrap justify-center gap-3">
        <Button onClick={handleCopy} variant="default">
          {copied ? (
            <Check className="h-4 w-4" />
          ) : (
            <Copy className="h-4 w-4" />
          )}
          {copied ? "Copied!" : "Copy Optimized Resume"}
        </Button>
        <Button onClick={handleExport} variant="outline">
          <Download className="h-4 w-4" />
          Export as Plain Text
        </Button>
        <Button onClick={onReset} variant="ghost">
          <RotateCcw className="h-4 w-4" />
          Start Over
        </Button>
      </div>
    </div>
  );
}
