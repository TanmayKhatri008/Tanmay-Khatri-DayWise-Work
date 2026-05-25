import { useState } from "react"

export default function Toggle()
{
    const [toggler, setToggler]  = useState(false);
    return(
        
        <div>
            <h1>Toggle</h1>
            <label>
                <input 
                checked = {toggler}
                type="checkbox"
                onChange={()=>{setToggler(!toggler)}}/>
            {toggler.toString()}
            </label>
            
        </div>
    )
}