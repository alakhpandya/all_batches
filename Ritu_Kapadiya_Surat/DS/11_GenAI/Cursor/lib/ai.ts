import { createOpenAI } from "@ai-sdk/openai";

const openai = createOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export const evalModel = openai(
  process.env.OPENAI_MODEL_EVAL ?? "gpt-4o-mini"
);

export const optimizeModel = openai(
  process.env.OPENAI_MODEL_OPTIMIZE ?? "gpt-4o"
);
