import "./globals.css";

export const metadata = {
  title: "My App",
  description: "Bootcamp Project",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-black text-white">
        {children}
      </body>
    </html>
  );
}
