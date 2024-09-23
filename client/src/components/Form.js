import React, { useState } from 'react';
import "../css/Form.css";

const Form = ({ addTask }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    status: 'Not Started'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then((response) => response.json())
      .then((data) => {
        addTask(data); 
        setFormData({
          title: '',
          description: '',
          status: 'Not Started'
        });
      })
      .catch((error) => console.error('Error adding task:', error));
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="horizontal-form">
        <div className="form-group">
          <label className="title"></label>
          <input
            type="text"
            id="title"
            name="title"
            placeholder="Name your task"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="description"></label>
          <input
            id="description"
            name="description"
            placeholder="Describe your task"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="status"></label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            required
          >
            <option value="Not Started">Not Started</option>
            <option value="In Progress">In Progress</option>
          </select>
        </div>
        <button className="form-button" type="submit">Add Task</button>
      </form>
    </div>
  );
};

export default Form;
