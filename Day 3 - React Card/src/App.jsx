import Card from "./components/Card"
import users from "./UserData/user"

function App(){

return(

<div className="min-h-screen bg-gray-100 p-10">

<h1 className="text-3xl font-bold text-center mb-10">
Profile Gallery
</h1>

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

{
users.map((user)=>(

<Card
key={user.id}
name={user.name}
role={user.role}
age={user.age}
experience={user.experience}
location={user.location}
image={user.image}
/>

))
}

</div>

</div>

)

}

export default App