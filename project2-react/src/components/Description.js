import NewsButton from './NewsButton'
import BMIButton from './BMIButton'

const Description = () => {
    return (
        <>
            <p>
                As the COVID vaccine continues...
                <br />
                Here goes much much more text that I don't really want to write
            </p>
            <NewsButton color='steelblue' text='News' />
            <BMIButton color='green' text='BMI' />
        </>
    )
}

export default Description
