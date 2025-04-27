
import './Row.css';
import { useEffect, useState } from 'react';

import { useNavigate } from 'react-router-dom';
import { useUserContext } from '../common/TestContext';
import {getMoreData} from '../services/UserServices.js'



function Row({isActive,rowData,scrollXa,ind}) {
  const [scrollX, setScrollX]=useState(localStorage.getItem('scroll'))
  const [curIndex, setCurrentIndex]=useState(parseInt(localStorage.getItem('index')))
  const navigate = useNavigate();
  // var items=[1,2,3,4,5,6,7,8,9,0,1,3,4,5,6,7,8,9,0]
  const { users, setUsers } = useUserContext();


  useEffect(() => {

    const fetchMoreData = async () => {
    
          try {
            const response = await getMoreData();
            var response1=JSON.stringify(response.data)
            response1=JSON.parse(response1)
    
            console.log(response1.rsp.payload.content)
    
            // console.log("App.js --> ",users)
            // console.log(response.data);
            // console.log("test data- >",response.rsp.payload.data)

            let temp =users

            temp[ind].content.push(...response1.rsp.payload.content)
            console.log("temp --> ",temp)
            setUsers(temp)
            console.log(users)
          } catch (error) {
            console.error('Failed to fetch users', error);
          } finally {
            // setLoading(false);
          }
        };


    const getScroll=(event)=>{
      console.log("length --> ",rowData.content.length," ",curIndex)
      let keyPres=event.keyCode
      switch(keyPres){
        case 37:{
            if(!isActive) return
            if(curIndex===0) return
            setScrollX(scrollX+50)
            setCurrentIndex(curIndex-1)
            break;
        }
        case 39:{
            if(!isActive) return
            if(curIndex===rowData.content.length-1) return
            setScrollX(scrollX-50)
            setCurrentIndex(curIndex+1)
            break;
        }
        default:{

        }
      }

      if(rowData.content.length-curIndex===5){
        console.log("call data2")
        fetchMoreData()
      }
      
      

    };

    window.addEventListener('keydown',getScroll)

    return()=>{
      window.removeEventListener('keydown',getScroll)
    }
  },[isActive, curIndex, scrollX, setUsers, users, rowData.content.length, ind])

 

  function onClickHandle(){
    localStorage.setItem('scroll',scrollX)
    localStorage.setItem('index',curIndex)
    navigate('/test')
  }


  // useEffect(() => {
  //   console.log("scroll ", rowNumber," ",scrollXa," ", scrollX)

  //   setScrollX(scrollXa)
  //   setCurrentIndex(ind)
  // },[scrollXa,ind])

  useEffect(() => {
   console.log("Row.Js",ind)
  },[ind])
  
  return (
    <div className="row">
        <div class='row' style={{transform: `translateX(${scrollX}vw)`, transition: 'transform 0.2s ease'}}>
            {rowData.content.map((item,index) => (
                <div class='item'>
                    <div class='item-content' onClick={onClickHandle}>
                        Test  {index} {scrollXa} {ind} {item}
                    </div>
                </div>
            ))}
        </div>
      
      
    </div>
  );
}

export default Row;
