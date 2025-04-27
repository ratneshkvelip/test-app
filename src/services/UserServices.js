import axios from 'axios'


const API_BASE_URL='http://localhost:9000'
export const getData=()=>{
    return axios.get(`${API_BASE_URL}/data1`);
}


export const getMoreData=()=>{
    console.log("called data2 api")
    return axios.get(`${API_BASE_URL}/data2`);
}