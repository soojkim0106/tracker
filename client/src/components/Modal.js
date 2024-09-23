import { useState, useEffect } from 'react';
import "../css/Modal.css";

const Modal = ({ task, onClose, onSubmit }) => {
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description);
  const [status, setStatus] = useState(task.status);

  useEffect(() => {
    setTitle(task.title);
    setDescription(task.description);
    setStatus(task.status);
  }, [task]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const updatedTask = { ...task, title, description, status };
    onSubmit(updatedTask);
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <form className="modal-form"onSubmit={handleSubmit}>
          <label className="modal-label">
            Title:
            <input className="modal-input" type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
          </label>
          <label className="modal-label">
            Description:
            <input className="modal-input" type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
          </label>
          <label className="modal-label">
            Status: &nbsp;
            <select value={status} onChange={(e) => setStatus(e.target.value)}>
              <option value="Not Started">Not Started</option>
              <option value="In Progress">In Progress</option>
              <option value="Completed">Completed</option>
            </select>
          </label>
          <button className="modal-button" type="submit">Save</button>
        </form>
      </div>
    </div>
  );
};

export default Modal;