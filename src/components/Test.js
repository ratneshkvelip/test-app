import { useNavigate } from "react-router-dom"

const Test =()=>{

    const navigate=useNavigate()

    return(
        <div>Test

            <button onClick={()=>{navigate('/')}}>Back</button>
        </div>
    )
}

export default Test