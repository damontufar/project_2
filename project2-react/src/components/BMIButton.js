const BMIButton = ({ text,color,onClick }) => {
    return (
        <button
            onClick={onClick}
            style={{ backgroundColor:color }}
            className='btn-bmi'
        >
            {text}
        </button>
    )
}

export default BMIButton
