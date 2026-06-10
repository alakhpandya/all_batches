import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Royal Technosoft ERP",
  description: "Ed-Tech ERP for Royal Technosoft",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
