import "./Modal.css";
import { useRef } from "react";
import axios from "axios";


function Modal({ onClose, children , user}) {
    const formData = useRef(null);
    const handleSubmit = (event) => {
        event.preventDefault();
        

        console.log(user);
        console.log(data);
        axios
        .post(`http://127.0.0.1:8000/transaction/${user}`, {
            amount: formData.current.amount.value,
            description: formData.current.description.value,
            type: formData.current.type.value,        
        },
        {
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
        });
    

        console.log(data);
        onClose();
    }

        


  return (
    <div className="Modal">
      <div className="Modal-overlay" onClick={onClose}>
        <div className="Modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="Close-btn" onClick={onClose}>
            &times;
            </button>
            <form className="Modal-form" ref={formData} onSubmit={handleSubmit}>
              <h2 className="Modal-title">Yangi ma'lumot</h2>
              <div className="Modal-input-group">
                <input type="number" id="amount" name="amount" placeholder="Miqdor" required />
              </div>
              <div className="Modal-input-group">
                <input type="text" id="description" name="description" placeholder="Tavsif" required />
              </div>
              <div className="Modal-input-group">
                <label htmlFor="type">Tur:</label>
                <select id="type" name="type" required>
                  <option value="income">Kirim</option>
                  <option value="expense">Chiqim</option>
                </select>
              </div>
              <button type="submit" className="Modal-submit-btn">Saqlash</button>
            </form>
        </div>
      </div>
    </div>
  );
}


export default Modal;