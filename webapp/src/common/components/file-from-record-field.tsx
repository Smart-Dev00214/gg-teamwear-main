import { useRecordContext } from "react-admin";
import { Link, Button } from "@mui/material";
import DownloadIcon from "@mui/icons-material/Download";

export function FileFromRecordField({
  source,
  filename,
}: {
  source: string;
  filename: (record) => string;
}) {
  const record = useRecordContext();

  return (
    <Button
      href={`data:text/plain;base64,${record[source]}`}
      variant="contained"
      startIcon={<DownloadIcon />}
      LinkComponent={Link}
      download={filename(record)}
    >
      Download
    </Button>
  );
}
