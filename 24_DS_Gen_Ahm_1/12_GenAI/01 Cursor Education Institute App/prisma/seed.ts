import { PrismaClient, Role } from "@prisma/client";
import bcrypt from "bcryptjs";

const prisma = new PrismaClient();

async function main() {
  const passwordHash = await bcrypt.hash("ChangeMe123!", 12);

  const superAdmin = await prisma.user.upsert({
    where: { email: "superadmin@royaltechnosoft.com" },
    update: {},
    create: {
      email: "superadmin@royaltechnosoft.com",
      passwordHash,
      name: "Super Admin",
      role: Role.SUPER_ADMIN,
    },
  });

  console.log("Seeded super admin:", superAdmin.email);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());
