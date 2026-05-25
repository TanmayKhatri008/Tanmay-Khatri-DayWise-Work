
import Card from "./Card";

export default function CardList() {
  const data = [
    {
      id: 1,
      name: "Aarav Sharma",
      role: "Frontend Developer",
      bio: "Passionate about building responsive and interactive web applications.",
      skills: ["React", "JavaScript", "CSS"],
      socialButtons: ["LinkedIn", "GitHub", "Portfolio"],
      
    },

    {
      id: 2,
      name: "Meera Joshi",
      role: "UI/UX Designer",
      bio: "Designs clean user experiences with a focus on accessibility.",
      skills: ["Figma", "Adobe XD", "Wireframing"],
      socialButtons: ["Dribbble", "Behance"],
      //// image: "https://example.com/profile2.jpg",
    },

    {
      id: 3,
      name: "Rohan Verma",
      role: "Backend Developer",
      bio: "Enjoys creating scalable APIs and database systems.",
      skills: ["Node.js", "Express", "MongoDB"],
      socialButtons: ["GitHub", "LinkedIn"],
      // image: "https://example.com/profile3.jpg",
    },

    {
      id: 4,
      name: "Ananya Singh",
      role: "Data Analyst",
      bio: "Transforms raw data into meaningful business insights.",
      skills: ["Python", "Pandas", "SQL"],
      socialButtons: ["LinkedIn", "Kaggle"],
      // image: "https://example.com/profile4.jpg",
    },

    {
      id: 5,
      name: "Kabir Mehta",
      role: "Mobile App Developer",
      bio: "Builds fast and user-friendly Android applications.",
      skills: ["Flutter", "Dart", "Firebase"],
      socialButtons: ["GitHub", "Play Store"],
      // image: "https://example.com/profile5.jpg",
    },

    {
      id: 6,
      name: "Priya Kapoor",
      role: "Cybersecurity Intern",
      bio: "Interested in ethical hacking and secure system design.",
      skills: ["Networking", "Linux", "Penetration Testing"],
      socialButtons: ["LinkedIn", "GitHub", "TryHackMe"],
      // image: "https://example.com/profile6.jpg",
    },

    {
      id: 7,
      name: "Dev Malhotra",
      role: "AI Engineer",
      bio: "Works on machine learning and intelligent automation systems.",
      skills: ["Python", "TensorFlow", "Deep Learning"],
      socialButtons: ["GitHub", "LinkedIn", "Hugging Face"],
      // image: "https://example.com/profile7.jpg",
    },

    {
      id: 8,
      name: "Sneha Iyer",
      role: "Cloud Engineer",
      bio: "Deploys and manages scalable cloud infrastructure.",
      skills: ["AWS", "Docker", "Kubernetes"],
      socialButtons: ["LinkedIn", "GitHub"],
      // image: "https://example.com/profile8.jpg",
    },

    {
      id: 9,
      name: "Yash Raj",
      role: "Game Developer",
      bio: "Loves creating immersive gameplay experiences.",
      skills: ["Unity", "C#", "Game Physics"],
      socialButtons: ["GitHub", "Itch.io", "Portfolio"],
      // image: "https://example.com/profile9.jpg",
    },

    {
      id: 10,
      name: "Ishita Bansal",
      role: "Full Stack Developer",
      bio: "Combines frontend and backend technologies to build complete applications.",
      skills: ["React", "Node.js", "PostgreSQL"],
      socialButtons: ["GitHub", "LinkedIn", "Portfolio"],
      // image: "https://example.com/profile10.jpg",
    },
  ];

  return(
    <>
    <div className="cardlist">
    {data.map(profile=>(
        <Card key = {profile.id} profile={profile}/>
    ))}
    </div>
    </>
  )
}
