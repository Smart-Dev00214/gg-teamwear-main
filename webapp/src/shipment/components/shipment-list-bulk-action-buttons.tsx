import {
  HttpError,
  useDataProvider,
  useListContext,
  useNotify,
} from "react-admin";
import { Button } from "@mui/material";
import { useMutation } from "react-query";
import { openPDFFromResponse } from "../../common/util/misc-util";

export function ShipmentListBulkActionButtons() {
  const { selectedIds } = useListContext();
  const dataProvider = useDataProvider();
  const notify = useNotify();
  const { isLoading, mutate } = useMutation(
    () => dataProvider.printTNTManifest(selectedIds),
    {
      retry: false,
      onError: (error: HttpError) => notify(error.message, { type: "error" }),
      onSuccess: async (data: Response) => {
        if (data.status !== 200) {
          const error = await data.json();
          notify(error.message, { type: "error" });
        } else {
          await openPDFFromResponse(data);
        }
      },
    }
  );

  return (
    <>
      <Button
        variant="contained"
        color="primary"
        onClick={() => mutate()}
        disabled={isLoading}
      >
        Print TNT Manifest
      </Button>
    </>
  );
}
