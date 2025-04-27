import { useNavigate } from "react-router-dom"

const Test =()=>{

    const navigate=useNavigate()

    return(
        <div>Test

            <button onClick={()=>{navigate('/home')}}>Back</button>
        </div>
    )
}

export default Test