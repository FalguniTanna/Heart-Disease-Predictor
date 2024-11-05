import React, { useState } from 'react';
import './Predictor.css';  // Link to enhanced CSS styles

const Predictor = () => {
    const [age, setAge] = useState('');
    const [sex, setSex] = useState('1');
    const [cp, setCp] = useState('0');
    const [trestbps, setTrestbps] = useState('');
    const [chol, setChol] = useState('');
    const [fbs, setFbs] = useState('0');
    const [restecg, setRestecg] = useState('0');
    const [thalch, setThalch] = useState('');
    const [exang, setExang] = useState('0');
    const [oldpeak, setOldpeak] = useState('');
    const [slope, setSlope] = useState('0');
    const [ca, setCa] = useState('0');
    const [thal, setThal] = useState('0');
    const [prediction, setPrediction] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: [
                    age,
                    sex,
                    '0',
                    cp,
                    trestbps,
                    chol,
                    fbs,
                    restecg,
                    thalch,
                    exang,
                    oldpeak,
                    slope,
                    ca,
                    thal
                ]
            }),
        });
        
        const result = await response.json();
        setPrediction(result.prediction);
    };

    return (
        <div className="predictor-container">
            <h1 className="title">Heart Disease Prediction</h1>
            <form onSubmit={handleSubmit} className="form-grid">
                <div className="form-group">
                    <label>Age</label>
                    <input type="number" placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Sex</label>
                    <select value={sex} onChange={(e) => setSex(e.target.value)}>
                        <option value="1">Male</option>
                        <option value="0">Female</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Chest Pain Type</label>
                    <select value={cp} onChange={(e) => setCp(e.target.value)}>
                        <option value="0">Typical Angina</option>
                        <option value="1">Atypical Angina</option>
                        <option value="2">Non-anginal Pain</option>
                        <option value="3">Asymptomatic</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Resting Blood Pressure</label>
                    <input type="number" placeholder="Resting BP" value={trestbps} onChange={(e) => setTrestbps(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Cholesterol</label>
                    <input type="number" placeholder="Cholesterol" value={chol} onChange={(e) => setChol(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Fasting Blood Sugar</label>
                    <select value={fbs} onChange={(e) => setFbs(e.target.value)}>
                        <option value="0">Less than 120</option>
                        <option value="1">Greater than 120</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Resting ECG</label>
                    <select value={restecg} onChange={(e) => setRestecg(e.target.value)}>
                        <option value="0">Normal</option>
                        <option value="1">ST-T Wave Abnormality</option>
                        <option value="2">Left Ventricular Hypertrophy</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Max Heart Rate</label>
                    <input type="number" placeholder="Max Heart Rate" value={thalch} onChange={(e) => setThalch(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Exercise Induced Angina</label>
                    <select value={exang} onChange={(e) => setExang(e.target.value)}>
                        <option value="0">No</option>
                        <option value="1">Yes</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Oldpeak</label>
                    <input type="number" placeholder="Oldpeak" value={oldpeak} onChange={(e) => setOldpeak(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Slope of ST Segment</label>
                    <select value={slope} onChange={(e) => setSlope(e.target.value)}>
                        <option value="0">Upsloping</option>
                        <option value="1">Flat</option>
                        <option value="2">Downsloping</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Number of Major Vessels</label>
                    <input type="number" placeholder="Number of Vessels" value={ca} onChange={(e) => setCa(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Thalassemia</label>
                    <select value={thal} onChange={(e) => setThal(e.target.value)}>
                        <option value="0">Normal</option>
                        <option value="1">Fixed Defect</option>
                        <option value="2">Reversible Defect</option>
                    </select>
                </div>
                <button type="submit" className="submit-btn">Predict</button>
            </form>
            {prediction && <h2 className={`prediction ${prediction === 'Heart Disease' ? 'danger' : 'safe'}`}>Prediction: {prediction}</h2>}
        </div>
    );
};

export default Predictor;
