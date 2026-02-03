'use client';
import React from 'react';

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
}

const Button: React.FC<ButtonProps> = ({ children, onClick }) => {
  return (
    <button
      className="px-4 py-3 bg-blue-400 text-black rounded hover:bg-blue-700"
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
