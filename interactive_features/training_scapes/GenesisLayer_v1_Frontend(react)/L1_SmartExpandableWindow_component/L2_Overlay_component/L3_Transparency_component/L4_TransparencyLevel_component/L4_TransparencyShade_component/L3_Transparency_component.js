import React from 'react';
import TransparencyShade from './TransparencyShade';
import TransparencyLevel from './TransparencyLevel';
import './TransparencyComponent.css';

function TransparencyComponent({ shade, level }) {
    return (
        <div className="transparency-component">
            <TransparencyShade shade={shade} />
            <TransparencyLevel level={level} />
            {/* Other child components or content can go here... */}
        </div>
    );
}

export default TransparencyComponent;