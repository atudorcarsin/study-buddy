import { LoginForm } from "@/components/login-form"
import {ModeToggle} from "@/components/theme/mode-toggle"

export default function LoginPage() {
  return (
    <div className="bg-muted flex min-h-svh flex-col items-center justify-center p-6 md:p-10">
      <div className="w-full max-w-sm md:max-w-3xl">
          <div className="absolute top-4 right-4">
              <ModeToggle />
          </div>
          <LoginForm />
      </div>
    </div>
  )
}
