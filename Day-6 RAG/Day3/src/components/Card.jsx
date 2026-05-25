export default function Card({profile})
{
    return(
        <>
            <div className="card">
                
                <img alt="item" src={profile.image || "https://cdn-icons-png.flaticon.com/512/149/149071.png" } />
                <h3>{profile.name}</h3>
                <h5>Role: {profile.role}</h5>
                <p>About: {profile.bio}</p>
                <ul>
                    {profile.skills.map((skill, index)=>(
                        <li key={index}> {skill} </li>
                    ))}
                </ul>
                <div>
                    {profile.socialButtons.map((btn, index)=>(
                        <button key ={index}> {btn}</button>
                    ))}
                </div>
                
            </div>
                
        </>
    )
}