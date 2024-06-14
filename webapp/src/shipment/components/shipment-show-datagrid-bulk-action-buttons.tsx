import { Button } from "@mui/material";
import { useListContext, useRecordContext } from "react-admin";
import DownloadIcon from "@mui/icons-material/Download";
import {
  b64DecodeUnicode,
  downloadFileFromBuffer,
} from "../../common/util/misc-util";

export function ShipmentShowDatagridBulkActionButtons() {
  const { data, selectedIds } = useListContext();
  const record = useRecordContext();

  const onClickDownloadButton = () => {
    const downloadBuffer: string[] = data
      .filter((datum) => selectedIds.includes(datum.id))
      .map((datum) => b64DecodeUnicode(datum.label));

    downloadFileFromBuffer(
      downloadBuffer,
      `bulk-shipping-labels-${record.shipmentIdentificationNumber}.zpl`
    );
  };

  return (
    <>
      <Button
        variant="contained"
        startIcon={<DownloadIcon />}
        onClick={onClickDownloadButton}
      >
        Download Bundle
      </Button>
    </>
  );
}
