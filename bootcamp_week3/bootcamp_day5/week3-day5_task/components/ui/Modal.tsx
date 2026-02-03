"use client";

export default function Modal({ open, onClose, children }: any) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white text-black p-6 rounded-xl shadow-xl w-[90%] max-w-md">
        {children}

        <button
          onClick={onClose}
          className="mt-4 bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
        >
          Close
        </button>
      </div>
    </div>
  );
}
