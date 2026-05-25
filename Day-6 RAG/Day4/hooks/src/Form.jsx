import { useEffect, useState } from "react"

export default function Form() {

    const [data, setData] = useState({ name: "", email: "" });
    const [all, setAll] = useState([]);

    const handleChange = (event) => {
        setData({ ...data, [event.target.name]: event.target.value });
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if (data.name && data.email) {
            setAll([...all, data]);
            setData({ name: "", email: "" });
        }
    }

    useEffect(() => {
        document.title = `${all.length} entr${all.length === 1 ? "y" : "ies"} submitted`;
    }, [all]);

    return (
        <>
            <h1>Form</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name: </label>
                <input
                    id="name"
                    type="text"
                    name="name"
                    value={data.name}
                    onChange={handleChange}
                />

                <label htmlFor="email">Email: </label>
                <input
                    id="email"
                    type="text"
                    name="email"
                    value={data.email}
                    onChange={handleChange}
                />
                <button type="submit">Submit</button>
            </form>

            <ul>
                {all.map((item, index) => (
                    <li key={index}>
                        Name: {item.name} — Email: {item.email}
                    </li>
                ))}
            </ul>
        </>
    )
}