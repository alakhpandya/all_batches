import { getToken } from "next-auth/jwt";
import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import { evaluateRouteAccess } from "@/lib/rbac";
import { getRoleHomePath } from "@/types/rbac";
import type { Role } from "@prisma/client";

export const config = {
  matcher: [
    /*
     * Run on all routes except static assets and Next internals.
     */
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  const token = await getToken({
    req: request,
    secret: process.env.NEXTAUTH_SECRET,
  });

  const session = token
    ? {
        user: {
          id: token.id as string,
          role: token.role as Role,
          isActive: Boolean(token.isActive),
          email: token.email as string | undefined,
          name: token.name as string | undefined,
        },
        expires: "",
      }
    : null;

  const decision = evaluateRouteAccess(pathname, session);

  if (!decision.allowed) {
    return NextResponse.redirect(new URL(decision.redirectTo, request.url));
  }

  // Authenticated users hitting /login → send to role home
  if (pathname === "/login" && session?.user?.role) {
    return NextResponse.redirect(
      new URL(getRoleHomePath(session.user.role), request.url),
    );
  }

  return NextResponse.next();
}
