import "./globals.css";
// import "./gooble.css"; // <-- add your custom css
import "./styles/google.css";


export const metadata = {
  title: "🤖 Cognitic AI Chat",
  description: "Talk to your Agentic AI powered by FastAPI",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
