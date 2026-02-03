export default function Badge({ children, variant = "default" }: any) {
  const styles = {
    default: "bg-blue-600 text-white",
    success: "bg-green-600 text-white",
    danger: "bg-red-600 text-white",
    warning: "bg-yellow-500 text-black",
  };

  return (
    <span className={`px-3 py-1 rounded-full text-sm ${styles[variant]}`}>
      {children}
    </span>
  );
}
