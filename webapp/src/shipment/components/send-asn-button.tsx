import { Button } from "@mui/material";
import {
  HttpError,
  useDataProvider,
  useNotify,
  useRecordContext,
} from "react-admin";
import { useMutation } from "react-query";
import { ShipmentStatusType } from "../values/shipment-status-choices";

export function SendASNButton() {
  const notify = useNotify();
  const record = useRecordContext();
  const dataProvider = useDataProvider();
  const { mutate, isLoading } = useMutation(
    () => dataProvider.sendASN(record.id),
    {
      retry: false,
      onError(error: HttpError) {
        notify(error.message, { type: "error" });
      },
      onSuccess() {
        notify("ASN sent", { type: "success" });
      },
    }
  );

  const handleClick = () => {
    mutate();
  };

  if (!record) return null;
  if (
    record &&
    ![ShipmentStatusType.CONFIRMED, ShipmentStatusType.NOTIFIED].includes(
      record.status
    )
  )
    return null;
  return (
    <Button
      variant="contained"
      color="primary"
      onClick={handleClick}
      disabled={isLoading}
    >
      Send ASN
    </Button>
  );
}
