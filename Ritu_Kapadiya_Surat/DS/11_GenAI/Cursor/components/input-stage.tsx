"use client";

import { FileText, Briefcase } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";

interface InputStageProps {
  resume: string;
  jobDescription: string;
  onResumeChange: (value: string) => void;
  onJobDescriptionChange: (value: string) => void;
  onOptimize: () => void;
  isDisabled?: boolean;
}

export function InputStage({
  resume,
  jobDescription,
  onResumeChange,
  onJobDescriptionChange,
  onOptimize,
  isDisabled,
}: InputStageProps) {
  return (
    <div className="space-y-6">
      <div className="grid gap-6 md:grid-cols-2">
        <Card className="flex flex-col">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-lg">
              <FileText className="h-5 w-5 text-primary" />
              Paste Original Resume
            </CardTitle>
            <CardDescription>
              Paste your entry-level IT resume text. Academic projects and
              coursework are supported.
            </CardDescription>
          </CardHeader>
          <CardContent className="flex-1">
            <Textarea
              placeholder="John Doe&#10;john.doe@email.com | (555) 123-4567&#10;&#10;EDUCATION&#10;B.S. Computer Science, State University, 2024&#10;&#10;PROJECTS&#10;• Built a Python data pipeline..."
              value={resume}
              onChange={(e) => onResumeChange(e.target.value)}
              className="min-h-[400px] resize-y font-mono text-sm"
            />
          </CardContent>
        </Card>

        <Card className="flex flex-col">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-lg">
              <Briefcase className="h-5 w-5 text-primary" />
              Paste Job Description
            </CardTitle>
            <CardDescription>
              Paste the full job description you are targeting.
            </CardDescription>
          </CardHeader>
          <CardContent className="flex-1">
            <Textarea
              placeholder="Junior Python Developer&#10;&#10;Requirements:&#10;• 0-2 years experience&#10;• Python, SQL, REST APIs&#10;• Bachelor's degree in CS or related field..."
              value={jobDescription}
              onChange={(e) => onJobDescriptionChange(e.target.value)}
              className="min-h-[400px] resize-y font-mono text-sm"
            />
          </CardContent>
        </Card>
      </div>

      <div className="flex justify-center">
        <Button
          size="lg"
          onClick={onOptimize}
          disabled={isDisabled || !resume.trim() || !jobDescription.trim()}
          className="min-w-[200px]"
        >
          Optimize Resume
        </Button>
      </div>
    </div>
  );
}
