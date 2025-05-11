import React, { use } from 'react'
import axios from 'axios'
import './App.css'
import { useState, useEffect } from 'react';
import Modal from './components/Modal';

function App() {

  const user = window.Telegram.WebApp.initDataUnsafe?.user;
  const userId = user.id;

  // userni telegram id, username va full_name ni olish 
  const [ transactions, setTransactions ] = useState(null);
  useEffect(() => {
  try{
  axios
  .post(`https://6c13-2a05-45c2-73f2-cc00-190c-4534-c65-b45.ngrok-free.app/user/`, {
    telegram_id: user.id,
    username: user.username,
    full_name: user.first_name,
  },{
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(response => {
    setTransactions(response.data);
  })
  .catch(error => {
    console.error('Error sending data:', error);
    console.log('Error details:', error.response.data);
  });}catch(TypeError){
    alert("Please open this bot in Telegram app");
  }
  }
  , []);



  // Modal ochish uchun
  const [isOpen, setIsOpen] = useState(false);


  // Modalni ochish va yopish
  const changeModal = () => {
    setIsOpen(!isOpen);
  }




  return (
    <>
    <div className="App">
      <div className="container">
          {transactions!== null &&
          <table  className='table'>
            {transactions && transactions.map((transaction) => (
              <tbody key={transaction.id}>
                  <tr>
                      <td>
                        <span className='tT'>
                        {transaction.type === 'income' ? '+' : '-'}
                        {transaction.amount}</span>
                      </td>
                      <td>
                        <span className='tD'>{transaction.description}</span><br />
                        <span className='tC'>{transaction.created_at}</span>
                      </td>
                  </tr>
              </tbody>
            ))}
          </table>
          }
      </div>

      {isOpen && <Modal user={userId} onClose={changeModal}></Modal>}

      <button className='newBtn' onClick={changeModal} >Yangi ma'lumot</button>
    <h1 className='bgText'>SOQQA</h1>
    </div>
    </>
  )
}

export default App
