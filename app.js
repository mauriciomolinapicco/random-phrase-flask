const express = require('express');
const app = express();
const port = 3000;

const frases = [
    "esto es una frase v1",
    "esto es una frase v2",
    "esto es una frase v3",
    "esto es una frase v4",
    "esto es una frase v5",
];

app.get('/frase', (req, res) => {
    const randomPhrase = frases[Math.floor(Math.random() * frases.length)];
    res.json({ phrase: randomPhrase });
});

app.get('/maximo', (req, res) => {
    const a = parseFloat(req.query.a);
    const b = parseFloat(req.query.b);

    if (isNaN(a) || isNaN(b)) {
        return res.status(400).json({ error: "Ambos parámetros deben ser números" });
    }

    const max = a > b ? a : b;
    res.json({ max });
});

app.listen(port, () => {
    console.log(`Servidor activo en el puerto 3000`);
});
