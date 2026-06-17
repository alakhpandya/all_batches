"use client";

interface ATSScoreRingProps {
  score: number;
  size?: number;
  strokeWidth?: number;
}

export function ATSScoreRing({
  score,
  size = 120,
  strokeWidth = 10,
}: ATSScoreRingProps) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;

  const color =
    score >= 85
      ? "stroke-emerald-500"
      : score >= 70
        ? "stroke-amber-500"
        : "stroke-red-500";

  const textColor =
    score >= 85
      ? "text-emerald-600"
      : score >= 70
        ? "text-amber-600"
        : "text-red-600";

  return (
    <div className="relative inline-flex items-center justify-center">
      <svg width={size} height={size} className="-rotate-90">
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="currentColor"
          strokeWidth={strokeWidth}
          className="text-muted/30"
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          className={`${color} transition-all duration-700 ease-out`}
        />
      </svg>
      <div className="absolute flex flex-col items-center">
        <span className={`text-2xl font-bold ${textColor}`}>{score}</span>
        <span className="text-xs text-muted-foreground">ATS Score</span>
      </div>
    </div>
  );
}
