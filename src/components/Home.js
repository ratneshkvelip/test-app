import '../App.css';
import { Suspense, useEffect, useState } from 'react';
import Row from './Row'

import Loader from './Loader.js'



import {getData} from '../services/UserServices.js'
import { useUserContext } from '../common/TestContext.js';


function Home() {
  const [scrollY, setScrollY]=useState(0)
  const [curIndex, setCurrentIndex]=useState(0)
  
  const [scrollX, setScrollX]=useState(0)
  const [curIndexX, setCurrentIndexX]=useState(0)
  const { users, setUsers } = useUserContext();


   useEffect(() => {
      fetchUsers();      
    }, []);
  
    const fetchUsers = async () => {
      try {
        const response = await getData();
        var response1=JSON.stringify(response.data)
        response1=JSON.parse(response1)

        console.log(response1.rsp.payload.data)

        // console.log("App.js --> ",users)
        // console.log(response.data);
        // console.log("test data- >",response.rsp.payload.data)
       

        setUsers(response1.rsp.payload.data)
        console.log(users)
      } catch (error) {
        console.error('Failed to fetch users', error);
      } finally {
        // setLoading(false);
      }
    };


  useEffect(()=>{
    let scro=localStorage.getItem('scroll1')
    let ind=localStorage.getItem('currentInd')
    if(scro===undefined || ind===undefined) return

    setScrollX(scro)
    setCurrentIndexX(ind)

  },[])

  useEffect(() => {
    console.log('test')
    const getScroll=(event)=>{
      console.log(curIndex)
      let keyPres=event.keyCode
      switch(keyPres){
        case 38:{
          if(curIndex===0) return
          setScrollY(scrollY+50)
   
          setCurrentIndex(curIndex-1)
          console.log(curIndex)
          break;
        }
        case 40:{
          if(curIndex===users.length-1) return
          setScrollY(scrollY-50)
          setCurrentIndex(curIndex+1)
          console.log(curIndex)
          break;
        }
        default:{

        }
      }

    };

    window.addEventListener('keydown',getScroll)

    return()=>{
      window.removeEventListener('keydown',getScroll)
    }
  },[curIndex, users.length, scrollY])


  
  return (
    <Suspense fallback={<Loader />}>
      <div className="App">
        <div class='group' style={{transform: `translateY(${scrollY}vh)`,transition: 'transform 2s ease'}}>
          {users.map((item,index) => (
                  <Row rowData={item} isActive={index===curIndex} ind={curIndex} scrollXa={scrollX}/>
            ))}
        </div>     
        
      </div>
    </Suspense>
    
  );
}

export default Home;
