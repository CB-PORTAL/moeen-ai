import React, { useState } from 'react';
import './OverlayComponent.css';

function OverlayComponent() {
    // State to keep track of whether the overlay is active or not
    const [isActive, setIsActive] = useState(false);

    // Function to handle click event
    const handleClick = () => {
        setIsActive(!isActive);
    };

    return (
        <div 
            className={`overlay ${isActive ? 'active' : ''}`} 
            onClick={handleClick}
        >
            {/* The overlay becomes visible on click and inactive on another click */}
        </div>
    );
}

export default OverlayComponent;