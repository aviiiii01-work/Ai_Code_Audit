"use client";

import { useState } from "react";
import Input from "@/components/ui/Input";
import Button from "@/components/ui/Button";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-gray-900 via-gray-700 to-black flex items-center justify-center p-6">

      <div className="w-full max-w-md bg-white/10 backdrop-blur-xl border border-white/20 p-10 rounded-2xl shadow-2xl">

        {/* Title */}
        <h1 className="text-3xl font-bold text-white text-center mb-8 tracking-wide">
          Welcome Back
        </h1>

        {/* Form */}
        <div className="flex flex-col gap-6">

          <Input
            label="Email"
            value={email}
            onChange={(e: any) => setEmail(e.target.value)}
            placeholder="Enter your email"
            className="h-12 bg-white/20 text-white placeholder-gray-300"
          />

          <Input
            label="Password"
            type="password"
            value={pass}
            onChange={(e: any) => setPass(e.target.value)}
            placeholder="Enter your password"
            className="h-12 bg-white/20 text-white placeholder-gray-300"
          />

          {/* Login Button */}
          <Button
            className="w-full h-12 text-lg font-semibold rounded-xl bg-white/90 text-gray-900 hover:bg-white transition-all"
            onClick={() => alert("Logged in")}
          >
            Login
          </Button>
        </div>

        {/* Footer */}
        <p className="mt-6 text-center text-sm text-gray-300">
          Don’t have an account?{" "}
          <span className="text-blue-400 cursor-pointer hover:underline">
            Sign Up
          </span>
        </p>
      </div>
    </div>
  );
}
