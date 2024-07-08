import * as React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
import Stack from '@mui/material/Stack';
import CircularProgress from '@mui/material/CircularProgress';
const cors = require('cors')

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

const Spin = () => {
  return (
    <Stack sx={{ color: "grey.500" }} spacing={2} direction="row">
      <CircularProgress color="secondary" />
      <CircularProgress color="success" />
      <CircularProgress color="inherit" />
    </Stack>
  );
};

function App() {
  const [articles, setArticles] = useState([]);
  const [load, setLoading] = useState(true)
  useEffect(
     () => {
      const fetchem = async () => {
        await axios.get("http://127.0.0.1:8000/inshamake/").then((res) => {
          setLoading(false)
          setArticles(res.data);
        });
      }
      fetchem();
  }, []);
  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <CssBaseline />
        <p variant="h2" style={{ padding: 10, margin: 4, fontSize: 30 }}>
          Newtimes latest news summary
        </p>

        <div style={{ padding: 10, margin: 4 }}>
          {load ? (<Spin />) : 
          (articles.map((art, index) => {
            console.log(art.umutwe);
            <Accordion key={index}>
              <AccordionSummary
                expandIcon={<ArrowDownwardIcon />}
                aria-controls="panel1-content"
                id="panel1-header"
              >
                <Typography>{art.umutwe}</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>{art.body}</Typography>
              </AccordionDetails>
            </Accordion>;
          }))}
        </div>
      </ThemeProvider>
    </>
  );
}

export default App;
