import { useState } from "react";
import axios from "axios";
import "./App.css";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

import Card from "@mui/material/Card";
// import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Typography from '@mui/material/Typography';

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

function App() {
  // api = 'http://127.0.0.1:8000/inshamake/'
  const [articles, setArticles] = useState([]);
  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <CssBaseline />
        <p variant="h2" style={{padding: 10, margin: 4, fontSize:30}}>
          Newstimes latest news summary
          </p>
        <Card sx={{ maxWidth: 300, padding: 3, margin: 4 }}>
          <CardContent>
            <Typography
              sx={{ fontSize: 14 }}
              color="text.secondary"
              gutterBottom
            >
              title
            </Typography>
            <Typography variant="body2">
              well meaning and kindly.
            </Typography>
          </CardContent>
        </Card>
      </ThemeProvider>
    </>
  );
}

export default App;
