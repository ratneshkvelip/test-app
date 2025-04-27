import { useEffect, useState } from 'react'
import './LandingPage.css'
import { useNavigate } from 'react-router-dom'
import {getData} from '../services/UserServices.js'

const LandingPage=()=>{
    const [profiles, setProfiles]=useState([])

    const navigate=useNavigate()

    useEffect(()=>{
        setProfiles([
            {
                profileId:"abc",
                profileName:"Ratnesh",
                prifileAvatar:"./mufasa.png"
            },
            {
                profileId:"xyz",
                profileName:"Guest",
                prifileAvatar:"./mufasa.png"
            }
        ])
    },[])

    const handleProfileSelect=()=>{
    
        navigate('/home')
    }

    return(
        <div class='profile-page'>

            <div class='profile-page-title' > Who's watching?</div>
            <div class='profiles-container'>
                {profiles.map((profile,index)=>(
                    <div class="profile-item">
                        <div class='profile-data'>
                            <div class='profile-avatar-container'><img src={profile.prifileAvatar} alt="" onClick={()=>handleProfileSelect(profile.profileId)}></img></div>
                            <div class='profile-name-container' onClick={()=>handleProfileSelect(profile.profileId)}> {profile.profileName}</div>
                        </div>
                    </div>
                )
                )}
                

            </div>

        </div>
    )
}


export default LandingPage