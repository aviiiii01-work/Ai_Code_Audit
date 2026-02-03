"use client";

export default function Input({
  label,
  type = "text",
  value,
  onChange,
  placeholder = "",
  className = "",
}: any) {
  return (
    <div className="flex flex-col gap-1 w-full">
      {label && <label className="text-sm font-medium text-white">{label}</label>}

      <input
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className={`px-3 py-2 rounded border border-gray-600 bg-zinc-800 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 ${className}`}
      />
    </div>
  );
}
