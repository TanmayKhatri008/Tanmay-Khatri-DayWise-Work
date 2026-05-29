function Card({ name, role, age, experience, location, image }) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-lg">
      <img
        src={image}
        className="w-24 h-24 rounded-full mx-auto"
        onError={(e) => {e.target.src = "/profile.png"}}/>

      <h2 className="text-xl font-bold text-center mt-3">{name}</h2>

      <p className="text-center text-gray-500">{role} </p>

      <div className="mt-4 space-y-2">
        <p> Age : {age}</p>
        <p> Experience : {experience}</p>
        <p> Location : {location}</p>
      </div>
    </div>
  );
}

export default Card;
