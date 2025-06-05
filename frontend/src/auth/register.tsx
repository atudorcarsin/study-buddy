import { RegisterForm } from "@/components/register-form"
import { ModeToggle } from "@/components/theme/mode-toggle"

export default function RegisterPage() {
  return (
    <div className="bg-muted flex min-h-svh flex-col items-center justify-center p-6 md:p-10">
      <div className="w-full max-w-sm md:max-w-3xl">
          <div className="absolute top-4 right-4">
              <ModeToggle />
          </div>
          <RegisterForm />
      </div>
    </div>
  )
}
