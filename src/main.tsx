import React from "react";
import { createRoot } from "react-dom/client";
import {
  ArrowUpRight,
  BrainCircuit,
  Code2,
  Download,
  Github,
  GraduationCap,
  Linkedin,
  Mail,
  Medal,
  ShieldCheck,
  Sparkles,
  Users
} from "lucide-react";
import "./styles.css";

type Project = {
  title: string;
  kicker: string;
  summary: string;
  role: string;
  stack: string[];
  metrics: string[];
  image: string;
  repo?: string;
  repoLabel?: string;
};

const projects: Project[] = [
  {
    title: "MalGuard-X",
    kicker: "Adversarial ML Research",
    summary:
      "Family-balanced malware image classification workflow combining adversarial training, Balanced Softmax, robust checkpoint selection, and Grad-CAM analysis.",
    role: "School-initiated CenTaD research project",
    stack: ["Python", "PyTorch", "EfficientNet", "MobileNetV3", "Grad-CAM"],
    metrics: [
      "FGSM, PGD-20, and PGD-50 evaluation",
      "Over 80% accuracy and macro-F1 in reported adversarial settings",
      "Robustness-first research workflow"
    ],
    image: "/assets/malguard-x.png",
    repo: "https://github.com/Russell-hci/centad-malguard",
    repoLabel: "View repository"
  },
  {
    title: "Project SPACE",
    kicker: "Applied Computer Vision",
    summary:
      "AI-powered accessible-parking monitoring workflow that detects vehicles, checks for mobility impairment labels, and captures license plates when misuse is suspected.",
    role: "Application tester, data collector, license-plate model training",
    stack: ["Python", "YOLOv8", "Roboflow", "Google Colab", "OpenCV"],
    metrics: [
      "Three-model detection flow",
      "208 uploaded images, 206 annotations, 510 augmented annotations",
      "Frame-by-frame video processing"
    ],
    image: "/assets/project-space.png"
  },
  {
    title: "Project SeatingPlan",
    kicker: "Full-Stack Education Tool",
    summary:
      "Teacher-focused seating-plan platform for creating, storing, and editing classroom layouts with drag-and-drop workflows and Firebase-backed user data.",
    role: "Seating plan generator logic and product workflow",
    stack: ["JavaScript", "React", "Bootstrap", "Firebase Auth", "Firebase Database"],
    metrics: [
      "Teacher interviews and feedback loop",
      "Real-time plan retrieval and storage",
      "Public project repository"
    ],
    image: "/assets/seatingplan.png",
    repo: "https://github.com/HCITanYR/seat",
    repoLabel: "View repository"
  },
  {
    title: "Pawnify Engine",
    kicker: "Interactive Engine UI",
    summary:
      "Browser-based chess GUI that makes engine customization approachable through FEN/PGN handling, clocks, takebacks, engine lines, evaluation, and custom starting positions.",
    role: "Project leader",
    stack: ["JavaScript", "Bootstrap", "Chess.js", "Chessboard.js", "Stockfish.js"],
    metrics: [
      "No-install chess bot customization",
      "Browser-to-engine messaging with Stockfish.js",
      "Private/archive case study"
    ],
    image: "/assets/pawnify.png"
  }
];

const focusAreas = [
  {
    title: "AI robustness",
    text: "Adversarial evaluation, family-balanced objectives, explainability, and practical model-selection discipline.",
    icon: ShieldCheck
  },
  {
    title: "Computer vision",
    text: "YOLO workflows for real-world detection tasks, from dataset planning and annotation to video processing.",
    icon: BrainCircuit
  },
  {
    title: "Full-stack prototypes",
    text: "Firebase-backed web apps, responsive interfaces, and product flows shaped around actual user needs.",
    icon: Code2
  },
  {
    title: "Agentic systems",
    text: "Interested in LLM applications, automation workflows, and startup environments where prototypes become working systems.",
    icon: Sparkles
  }
];

const achievements = [
  "19th Place, Cyberthon 2026",
  "23rd Place, BrainHack TIL-AI 2026 (Novice Track)",
  "Gold Award, QCEC 2025",
  "Outstanding Student Award",
  "Microsoft AI & ML Engineering Professional Certificate",
  "Financial Technology Innovations Specialization"
];

function ExternalLink({ href, children }: { href: string; children: React.ReactNode }) {
  return (
    <a href={href} target="_blank" rel="noreferrer" className="button button-secondary">
      {children}
      <ArrowUpRight size={16} aria-hidden="true" />
    </a>
  );
}

function App() {
  return (
    <main>
      <section className="hero" aria-labelledby="intro-title">
        <nav className="topbar" aria-label="Primary">
          <a href="#work">Work</a>
          <a href="#focus">Focus</a>
          <a href="#leadership">Leadership</a>
          <a href="#contact">Contact</a>
        </nav>

        <div className="hero-grid">
          <div className="hero-copy">
            <p className="eyebrow">JC1 student developer · Singapore</p>
            <h1 id="intro-title">Yap Ming Xuan</h1>
            <p className="lede">
              Building applied AI, computer vision, and full-stack prototypes with a startup-oriented bias for
              turning ambiguous ideas into working systems.
            </p>
            <div className="hero-actions" aria-label="Primary links">
              <a className="button button-primary" href="/Yap_Ming_Xuan_Resume_Public.pdf">
                <Download size={16} aria-hidden="true" />
                Resume
              </a>
              <ExternalLink href="https://github.com/Russell-hci">
                <Github size={16} aria-hidden="true" />
                GitHub
              </ExternalLink>
              <ExternalLink href="https://www.linkedin.com/in/russellmx">
                <Linkedin size={16} aria-hidden="true" />
                LinkedIn
              </ExternalLink>
              <a className="button button-secondary" href="mailto:221541b@student.hci.edu.sg">
                <Mail size={16} aria-hidden="true" />
                Email
              </a>
            </div>
          </div>

          <aside className="signal-panel" aria-label="Profile summary">
            <div>
              <span className="panel-label">Current focus</span>
              <strong>AI engineering, CV systems, agentic workflows</strong>
            </div>
            <div>
              <span className="panel-label">Leadership</span>
              <strong>Machine Learning Section Head, Hwa Chong IRS</strong>
            </div>
            <div>
              <span className="panel-label">Portfolio signal</span>
              <strong>Research + applied systems + web product delivery</strong>
            </div>
          </aside>
        </div>
      </section>

      <section className="section" id="work" aria-labelledby="work-heading">
        <div className="section-heading">
          <p className="eyebrow">Selected work</p>
          <h2 id="work-heading">Projects with technical depth and product shape</h2>
        </div>
        <div className="project-grid">
          {projects.map((project) => (
            <article className="project-card" key={project.title}>
              <img src={project.image} alt="" />
              <div className="project-body">
                <p className="kicker">{project.kicker}</p>
                <h3>{project.title}</h3>
                <p>{project.summary}</p>
                <p className="role">{project.role}</p>
                <div className="chip-row" aria-label={`${project.title} stack`}>
                  {project.stack.map((item) => (
                    <span key={item}>{item}</span>
                  ))}
                </div>
                <ul>
                  {project.metrics.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
                {project.repo ? (
                  <a className="text-link" href={project.repo} target="_blank" rel="noreferrer">
                    {project.repoLabel}
                    <ArrowUpRight size={15} aria-hidden="true" />
                  </a>
                ) : (
                  <span className="text-note">Case study available on request</span>
                )}
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="section section-band" id="focus" aria-labelledby="focus-heading">
        <div className="section-heading">
          <p className="eyebrow">Engineering focus</p>
          <h2 id="focus-heading">Where I am aiming my learning curve</h2>
        </div>
        <div className="focus-grid">
          {focusAreas.map(({ title, text, icon: Icon }) => (
            <article className="focus-item" key={title}>
              <Icon size={22} aria-hidden="true" />
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section split" id="leadership" aria-labelledby="leadership-heading">
        <div>
          <p className="eyebrow">Leadership</p>
          <h2 id="leadership-heading">Technical work, mentoring, and communication</h2>
        </div>
        <div className="timeline">
          <article>
            <Users size={20} aria-hidden="true" />
            <div>
              <h3>Machine Learning Section Head</h3>
              <p>
                Lead the ML division within Hwa Chong Institution's Infocomm & Robotics Society, guiding members in AI,
                machine learning, and software project development.
              </p>
            </div>
          </article>
          <article>
            <GraduationCap size={20} aria-hidden="true" />
            <div>
              <h3>Volunteer Instructor, FutureTech</h3>
              <p>
                Taught programming, technology, and digital-literacy concepts to Primary 5 to Secondary 2 students
                through hands-on lessons.
              </p>
            </div>
          </article>
          <article>
            <Medal size={20} aria-hidden="true" />
            <div>
              <h3>Achievements and certifications</h3>
              <div className="achievement-list">
                {achievements.map((achievement) => (
                  <span key={achievement}>{achievement}</span>
                ))}
              </div>
            </div>
          </article>
        </div>
      </section>

      <section className="contact" id="contact" aria-labelledby="contact-heading">
        <p className="eyebrow">Contact</p>
        <h2 id="contact-heading">Open to AI engineering, startup, and applied software opportunities.</h2>
        <div className="hero-actions">
          <a className="button button-primary" href="mailto:221541b@student.hci.edu.sg">
            <Mail size={16} aria-hidden="true" />
            221541b@student.hci.edu.sg
          </a>
          <a className="button button-secondary" href="/Yap_Ming_Xuan_Resume_Public.pdf">
            <Download size={16} aria-hidden="true" />
            Download resume
          </a>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
