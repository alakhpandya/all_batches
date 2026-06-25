"use client";

import { useReducer, useState, useEffect, useCallback, useRef } from "react";
import { Sparkles } from "lucide-react";
import { InputStage } from "@/components/input-stage";
import { ProcessingStage } from "@/components/processing-stage";
import { OutputStage } from "@/components/output-stage";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import type { OptimizeResponse, OptimizeErrorResponse } from "@/lib/types";

type Stage = "input" | "processing" | "output";

interface AppState {
  stage: Stage;
  currentStep: number;
  result: OptimizeResponse | null;
  error: string | null;
}

type Action =
  | { type: "START" }
  | { type: "SET_STEP"; step: number }
  | { type: "SUCCESS"; data: OptimizeResponse }
  | { type: "ERROR"; message: string }
  | { type: "RESET" };

const initialState: AppState = {
  stage: "input",
  currentStep: 0,
  result: null,
  error: null,
};

function reducer(state: AppState, action: Action): AppState {
  switch (action.type) {
    case "START":
      return {
        ...state,
        stage: "processing",
        currentStep: 0,
        result: null,
        error: null,
      };
    case "SET_STEP":
      return { ...state, currentStep: action.step };
    case "SUCCESS":
      return {
        ...state,
        stage: "output",
        result: action.data,
        error: null,
      };
    case "ERROR":
      return {
        ...state,
        stage: "input",
        error: action.message,
      };
    case "RESET":
      return initialState;
    default:
      return state;
  }
}

const PROCESSING_STEPS = 4;
const STEP_INTERVAL_MS = 3000;

export default function Home() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const [resume, setResume] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const abortRef = useRef<AbortController | null>(null);

  const handleOptimize = useCallback(async () => {
    dispatch({ type: "START" });
    abortRef.current?.abort();
    abortRef.current = new AbortController();

    try {
      const response = await fetch("/api/optimize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ resume, jobDescription }),
        signal: abortRef.current.signal,
      });

      const data = await response.json();

      if (!response.ok) {
        const err = data as OptimizeErrorResponse;
        dispatch({
          type: "ERROR",
          message: err.error ?? "Optimization failed.",
        });
        return;
      }

      dispatch({ type: "SUCCESS", data: data as OptimizeResponse });
    } catch (err) {
      if (err instanceof DOMException && err.name === "AbortError") return;
      dispatch({
        type: "ERROR",
        message: "Network error. Please check your connection and try again.",
      });
    }
  }, [resume, jobDescription]);

  useEffect(() => {
    if (state.stage !== "processing") return;

    let step = 0;
    const interval = setInterval(() => {
      step = Math.min(step + 1, PROCESSING_STEPS - 1);
      dispatch({ type: "SET_STEP", step });
    }, STEP_INTERVAL_MS);

    return () => clearInterval(interval);
  }, [state.stage]);

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <header className="mb-10 text-center">
          <div className="mb-3 flex items-center justify-center gap-2">
            <Sparkles className="h-8 w-8 text-primary" />
            <h1 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
              ATS-Max
            </h1>
          </div>
          <p className="text-lg text-muted-foreground">
            Iterative Resume Optimizer for Entry-Level IT Roles
          </p>
          <p className="mt-1 text-sm text-muted-foreground">
            Transform your resume to pass Applicant Tracking Systems with a score
            of 85+
          </p>
        </header>

        {state.error && (
          <Alert variant="destructive" className="mb-6">
            <AlertTitle>Optimization Failed</AlertTitle>
            <AlertDescription>{state.error}</AlertDescription>
          </Alert>
        )}

        {state.stage === "input" && (
          <InputStage
            resume={resume}
            jobDescription={jobDescription}
            onResumeChange={setResume}
            onJobDescriptionChange={setJobDescription}
            onOptimize={handleOptimize}
          />
        )}

        {state.stage === "processing" && (
          <ProcessingStage currentStep={state.currentStep} />
        )}

        {state.stage === "output" && state.result && (
          <OutputStage
            data={state.result}
            originalResume={resume}
            onReset={() => dispatch({ type: "RESET" })}
          />
        )}
      </div>
    </main>
  );
}
